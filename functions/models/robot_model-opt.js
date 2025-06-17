// This Pages Function serves a .glb file directly from Cloudflare R2.
// It assumes your R2 bucket is bound as 'MODEL_BUCKET' in your Cloudflare Pages settings.

export async function onRequest(context) {
    const { env, request } = context; // 'env' gives access to R2 bindings, 'request' is the incoming HTTP request

    // Define the key for your GLB file in the R2 bucket.
    // This should match the exact path and filename as stored in R2.
    const r2ObjectKey = 'robot_model-opt.glb'; 

    try {
        // Attempt to get the object from your R2 bucket.
        // env.MODEL_BUCKET refers to the R2 binding you set up.
        const object = await env.MODEL_BUCKET.get(r2ObjectKey);

        // If the object is not found in R2, return a 404 Not Found response.
        if (object === null) {
            console.warn(`GLB file '${r2ObjectKey}' not found in R2 bucket.`);
            return new Response('Not Found', { status: 404 });
        }

        // Create headers for the response.
        const headers = new Headers();

        // Automatically set standard HTTP metadata (like Content-Length) from the R2 object.
        object.writeHttpMetadata(headers);

        // Crucially, set the correct Content-Type for .glb files.
        // This tells the browser how to interpret the file.
        headers.set('Content-Type', 'model/gltf-binary');

        // Set ETag for caching and conditional requests.
        headers.set('ETag', object.httpEtag);

        // Optional: Add caching headers to allow browsers and CDNs to cache the file.
        // 'public' means it can be cached by proxies, 'max-age' specifies the cache duration in seconds.
        // Adjust max-age as appropriate for how often this file might change.
        headers.set('Cache-Control', 'public, max-age=31536000, immutable'); // Cache for 1 year, immutable for unchanging assets

        // Return the object's body (the file content) with the configured headers and a 200 OK status.
        return new Response(object.body, {
            headers,
            status: 200,
        });

    } catch (error) {
        // Log any errors that occur during the R2 fetch operation.
        console.error('Error serving GLB file from R2:', error);
        // Return a 500 Internal Server Error response in case of an unexpected error.
        return new Response('Internal Server Error', { status: 500 });
    }
}
