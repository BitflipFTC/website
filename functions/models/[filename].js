export async function onRequest({ env, params }) {
  // params.filename will capture the part of the URL after /models/,
  // including the .glb extension (e.g., "robot_model-opt.glb")
  const r2ObjectKey = params.filename; 

  const object = await env.MODEL_BUCKET.get(r2ObjectKey); // Use env.MODEL_BUCKET as per your binding name

  if (object === null) {
    // Log this for debugging if it still fails
    console.error(`R2 object not found for key: ${r2ObjectKey} in bucket ${env.MODEL_BUCKET.name}`); 
    return new Response('3D Model Not Found', { status: 404 });
  }

  const headers = new Headers();
  object.writeHttpMetadata(headers); // Writes Last-Modified, Content-Length etc.
  headers.set('ETag', object.httpEtag);
  headers.set('Content-Type', 'model/gltf-binary'); // Crucial for GLB files

  return new Response(object.body, {
    headers,
  });
}