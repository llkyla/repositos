"use strict";
var gl;
var points;


function init()
{
    var canvas = document.getElementById( "gl-canvas" );

    gl = canvas.getContext('webgl2');
    if ( !gl ) { alert( "WebGL isn't available" ); }
    
    points=[];
    points.push(vec2(Math.random().toFixed(2),Math.random().toFixed(2)));
    points.push(vec2(Math.random().toFixed(2),Math.random().toFixed(2)));
    points.push(vec2(-Math.random().toFixed(2),-Math.random().toFixed(2)));
    points.push(vec2(Math.random().toFixed(2),-Math.random().toFixed(2)));

    //
    //  Configure WebGL
    //
    gl.viewport( 0, 0, canvas.width, canvas.height );
    gl.clearColor( 1.0, 1.0, 1.0, 1.0 );

    //  Load shaders and initialize attribute buffers

    var program = initShaders( gl, "vertex-shader", "fragment-shader" );
    gl.useProgram( program );

    // Load the data into the GPU

    var bufferId = gl.createBuffer();
    gl.bindBuffer( gl.ARRAY_BUFFER, bufferId );
    gl.bufferData( gl.ARRAY_BUFFER, flatten(points), gl.STATIC_DRAW );

    // Associate out shader variables with our data buffer

    var position = gl.getAttribLocation( program, "aPosition" );
    gl.vertexAttribPointer( position , 2, gl.FLOAT, false, 0, 0 );
    gl.enableVertexAttribArray( position );

    render();
};

function render() {
    gl.clear( gl.COLOR_BUFFER_BIT );
    gl.drawArrays( gl.POINTS, 0, points.length );
}