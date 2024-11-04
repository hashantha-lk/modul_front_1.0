let drawingStraightLine = false;
let drawingCurve = false;
let startPoint;
let currentLine;
let erasingMode = false;
let markingPointsMode = false;

document.addEventListener('DOMContentLoaded', function () {
    const canvas = new fabric.Canvas('canvas');
    window.canvas = canvas;
    document.getElementById('file-input').addEventListener('change', function (e) {
        const file = e.target.files[0];
        const formData = new FormData();
        formData.append('file', file);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    console.error('Server returned an error:', data.error);
                    alert(data.error);
                } else {
                    console.log('File uploaded successfully:', data.file_path);
                    const imageUrl = `/uploads/${data.file_path.split('/').pop()}`;
                    console.log('Constructed image URL:', imageUrl);
                    fabric.Image.fromURL(imageUrl, function (img) {
                        if (!img) {
                            console.error('Failed to load image:', imageUrl);
                            return;
                        }
                        img.scaleToWidth(canvas.width);
                        img.scaleToHeight(canvas.height);
                        canvas.setBackgroundImage(img, canvas.renderAll.bind(canvas));
                        console.log('Image loaded and set as background');
                    }, null, { crossOrigin: 'anonymous' });

                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });

});

/* Line */
function setDrawStraightLineMode() {
    drawingStraightLine = true;
    drawingCurve = false;
    erasingMode = false;
    markingPointsMode = false;
    canvas.isDrawingMode = false;
    canvas.selection = false;


    let startX, startY, line;

    canvas.on('mouse:down', function (event) {
        if (drawingStraightLine) {
            const pointer = canvas.getPointer(event.e);
            startX = pointer.x;
            startY = pointer.y;
            line = new fabric.Line([startX, startY, startX, startY], {
                stroke: 'yellow',
                strokeWidth: 3,
                selectable: false,
                evented: false
            });
            canvas.add(line);
        }
    });

    canvas.on('mouse:move', function (event) {
        if (drawingStraightLine && line) {
            const pointer = canvas.getPointer(event.e);
            line.set({ x2: pointer.x, y2: pointer.y });
            canvas.renderAll();
        }
    });

    canvas.on('mouse:up', function () {
        line = null;
    });
}

/* Curve */
function setDrawCurveMode() {
    drawingStraightLine = false;
    drawingCurve = true;
    erasingMode = false;
    markingPointsMode = false;
    canvas.isDrawingMode = true;
    canvas.freeDrawingBrush = new fabric.PencilBrush(canvas);
    canvas.freeDrawingBrush.width = 3;
    canvas.freeDrawingBrush.color = 'yellow';
}

function setDrawMode() {
    drawingStraightLine = false;
    drawingCurve = false;
    erasingMode = false;
    markingPointsMode = false;
    canvas.isDrawingMode = true;
    canvas.freeDrawingBrush = new fabric.PencilBrush(canvas);
    canvas.freeDrawingBrush.width = 3;
    canvas.freeDrawingBrush.color = 'yellow';
    canvas.selection = true;
    canvas.forEachObject(function (obj) {
        obj.selectable = true;
    });
}

/* Mark Points */
function setMarkPointMode() {
    drawingStraightLine = false;
    drawingCurve = false;
    erasingMode = false;
    markingPointsMode = true;
    canvas.isDrawingMode = false;
    canvas.selection = false;

    canvas.on('mouse:down', function (options) {
        if (markingPointsMode) {
            const pointer = canvas.getPointer(options.e);
            const circle = new fabric.Circle({
                radius: 5,
                fill: 'red',
                left: pointer.x,
                top: pointer.y,
                selectable: false,
                evented: false
            });
            const pointName = prompt('Enter point name:');
            const text = new fabric.Textbox(pointName, {
                left: pointer.x + 10,
                top: pointer.y,
                fontSize: 16,
                fontWeight: 'bold',
                fill: 'black',
                backgroundColor: 'white',
                selectable: false,
                evented: false
            });

            const group = new fabric.Group([circle, text], {
                left: pointer.x,
                top: pointer.y,
                selectable: false,
                evented: false
            });

            canvas.add(group);
        }
    });
}

/* Undo */
function undoLastAction() {
    const lastObject = canvas.getObjects().pop();
    if (lastObject) {
        canvas.remove(lastObject);
        redoStack.push(lastObject);

    }
}

/* Redo */
const redoStack = [];
function redoLastAction() {
    const lastUndoneObject = redoStack.pop();
    if (lastUndoneObject) {
        canvas.add(lastUndoneObject);
        redoStack.push(lastObject);

    }
}
/* Clear Canvas */
function clearCanvas() {
    const objects = canvas.getObjects();
    while (objects.length) {
        const object = objects.pop();
        canvas.remove(object);
        redoStack.push(object);
    }
}

/* Save */
function saveCanvas() {
    const dataURL = canvas.toDataURL({
        format: 'png',
        quality: 1
    });
    const link = document.createElement('a');
    link.href = dataURL;
    link.download = 'canvas.png';
    link.click();
}



canvas.on('mouse:down', function (options) {
    if (markingPointsMode) {
        const pointer = canvas.getPointer(options.e);
        const circle = new fabric.Circle({
            radius: 5,
            fill: 'red',
            left: pointer.x,
            top: pointer.y
        });
        const text = new fabric.Textbox(prompt('Enter point name:'), {
            left: pointer.x + 10,
            top: pointer.y - 10,
            fontSize: 16,
            fill: 'black'
        });
        canvas.add(circle, text);
    }
});

