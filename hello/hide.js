// chrome.tabs.executeScript(null,{code:`
// fetch('http://localhost:5000/data', {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({url: window.location.href})
// })
// .then(response => response.json())
// .then(data => {
     //var url = data.url;
  arr =  ["https://cheery-mermaid-32f0cb.netlify.app/obsc/I1.jpeg","https://cheery-mermaid-32f0cb.netlify.app/obsc/I2.jpeg","https://cheery-mermaid-32f0cb.netlify.app/obsc/I3.jpeg","https://cheery-mermaid-32f0cb.netlify.app/obsc/I4.jpeg","https://cheery-mermaid-32f0cb.netlify.app/obsc/I5.jpeg","https://cheery-mermaid-32f0cb.netlify.app/obsc/I6.jpeg","https://cheery-mermaid-32f0cb.netlify.app/misc/OIP%20(11).jpeg","https://cheery-mermaid-32f0cb.netlify.app/misc/OIP%20(5).jpeg","https://cheery-mermaid-32f0cb.netlify.app/misc/OIP%20(16).jpeg","https://cheery-mermaid-32f0cb.netlify.app/misc/OIP%20(24).jpeg","https://cheery-mermaid-32f0cb.netlify.app/misc/OIP%20(29).jpeg","https://cheery-mermaid-32f0cb.netlify.app/misc/OIP%20(7).jpeg"];
     h = document.querySelectorAll('img');

     for (i = 0; i < arr.length; i++) {
         for (j = 0; j < h.length; j++) {
             if (h[j].src === arr[i]) {
                 h[j].style.filter = 'blur(20px)';
             }
         }
     }

     setTimeout(function() {
         alert('Obscene detected ' + arr.length);
     }, 100);
// });
// `});


//  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
//    chrome.tabs.executeScript(tabs[0].id, {
//      code: `fetch('http://localhost:5000/data')
//      .then(response => response.json())
//      .then(data => {
        // arr = ["https://cheery-mermaid-32f0cb.netlify.app/obsc/I1.jpeg","https://cheery-mermaid-32f0cb.netlify.app/obsc/I5.jpeg","https://cheery-mermaid-32f0cb.netlify.app/obsc/I6.jpeg","https://cheery-mermaid-32f0cb.netlify.app/misc/OIP%20(7).jpeg"]; // Assign the array to a local variable
        // images = document.querySelectorAll('img');
        // for (i = 0; i < arr.length; i++) {
        //   for (j = 0; j < images.length; j++) {
        //     if (images[j].src == arr[i]) {
        //       images[j].style.filter = 'blur(20px)';
        //     }
        //   }
        // }
        // setTimeout(function() {
        //   alert('Obscene images detected: ' + arr.length);
        // }, 100)
//      });
//    });
 
// xmlhttp = new XMLHttpRequest();
// xmlhttp.onreadystatechange = function() {
//   //if (this.readyState == 4 && this.status == 200) {
//     const arr = this.responseText.split('\n');
//     console.log(arr); // array of image sources
//     images = document.querySelectorAll('img');
//      for (i = 0; i < arr.length; i++) {
//           for (j = 0; j < images.length; j++) {
//                if (images[j].src == arr[i]) {
//                     images[j].style.filter = 'blur(20px)';
//                }
//           } 
//      }
//      for(i=0;i<arr.length;i++){
//           alert(arr[i])}
//   //}
// };
// xmlhttp.open("GET", "t.txt", true);
// xmlhttp.send();
// let input = document.querySelector('input');
// let textarea = document.querySelector('textarea');
// input.addEventListener('change', () => {
//     let files = input.files;
//     if(files.length == 0) return;
//     const file = files[0];
//     let reader = new FileReader();
//     reader.onload = (e) => {
//         const file = e.target.result;
//         const lines = file.split(/\r\n|\n/);
//         textarea.value = lines.join('\n');
//     };
//     reader.onerror = (e) => alert(e.target.error.name);
//     reader.readAsText(file); 
    
// });


// fetch('http://localhost:5000/data',
//  {
//      method:'POST',
//      (response=>response.json())
//      (data=>{
//         let reader=new FileReader();
//     let files=input.files;
//     if(files.length==0) return;
//     reader.onload=(e)=>{
//     const file=e.target.result;
//     const lines=file.split(/r\n|\n/);
//     textarea.value=lines.join('\n');
//     images=reader.readAsArrayBuffer(file);
// };
//     for (let i = 0; i < arr.length; i++) {
//              for (let j = 0; j < images.length; j++) {
//                if (images[j].src == arr[i]) {
//                  images[j].style.filter = 'blur(20px)';
//                }
//              }
//             }
//      })
//  })

//  fetch('http://localhost:5000/data', {
//   method: 'POST',
//   headers: {
//     'Content-Type': 'application/json;charset=UTF-8'
//   },
//   body: JSON.stringify({url: window.location.href})
// })
// .then(response => {
//   if (!response.ok) {
//     throw new Error('Network response was not ok');
//   }
//   return response.json();
// })
// .then(data => {
//   console.log(data); // log the fetched data to the console
 // arr = data.my_array; // Assign the array to a local variable
//  arr=["https://cheery-mermaid-32f0cb.netlify.app/obsc/I1.jpeg","https://cheery-mermaid-32f0cb.netlify.app/obsc/I5.jpeg","https://cheery-mermaid-32f0cb.netlify.app/obsc/I6.jpeg","https://cheery-mermaid-32f0cb.netlify.app/misc/OIP%20(7).jpeg"]
//   images = document.querySelectorAll("img");
//   for(i = 0; i < arr.length; i++) {
//     for(j = 0; j < images.length; j++) {
//       if(images[j].src === arr[i]) {
//         images[j].style.filter = "blur(20px)";
//       }
//     }
//   }
//   setTimeout(function() {
//     alert("Obscene detected " + arr.length);
//   }, 100);
// })  
// .catch(error => console.error('Error:', error));