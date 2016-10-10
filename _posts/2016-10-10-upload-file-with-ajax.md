---
layout: post
title: Upload file using javascript with ajax
---

We can upload files to the server using javascript with the help of **FormData** object.

Inorder to do that, let's firt create a controller which attempts to serve the file upload call from front-end.

    @RequestMapping(value = "/upload", method = RequestMethod.POST)
    @ResponseBody
    public void upload(@RequestParam("file") MultipartFile file) {
        String rawFile = file.getContentType();
        System.out.println();
    }

After deploying the server with the above code, we can send data to **http://localhost:8080/upload** to make our server accepts data from front-end.
So the nest step is to make the javascript to send the data of the file we choose.

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Upload File</title>
    </head>
    <body>
    
    <form id="file-form" method="POST">
        <input type="file" id="file-select">
        <button type="submit" id="upload-button">Upload</button>
    </form>

    <script>
        var form = document.getElementById('file-form');
        var fileSelect = document.getElementById('file-select');
        var uploadButton = document.getElementById('upload-button');
        uploadButton.addEventListener('click', function (event) {
            var formData = new FormData();
            var file = fileSelect.files[0];
            formData.append('file', file);
            
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'http://localhost:8080/upload', true);
            xhr.send(formData);
        });
    </script>
    </body>
    </html>
    
The above code basically attempts to create a **FormData** with metadata of the selected file. Then the code creates an **XMLHttpRequest** which sends the **FormData**
to the specific url destination. After everything is configured, you may check the uploaded file at the server side through debugger.
