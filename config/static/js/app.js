
function saludar() {
    let email = document.getElementById("exampleInputEmail1")
    alert("Hola Mundo "+ email.value);
}

      function SaveUser() {
       
        let emailInput = document.getElementById("exampleInputEmail1");
        let fullnameInput = document.getElementById("FullName");
        let tbody = document.getElementById("tcuerpo");
        let endpoint  = "/controller/Saveuser";
       
        let email = emailInput.value;
        let fullname = fullnameInput.value;
        
        axios.post(endpoint, {
            'fullname': fullname,
            'email': email
          })
          .then(function (response) {
           
            swal("Good job!", "datos Guardados", "success");
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          })
          .finally(function () {
            // siempre sera ejecutado
          });
          cargadatos();
        
        let newRow = document.createElement("tr");
        newRow.innerHTML = `
            <th scope="row">${tbody.children.length + 1}</th>
            <td>${email}</td>
            <td>${fullname}</td>
        `;
    
        
        tbody.appendChild(newRow);
       
        emailInput.value = "";
        fullnameInput.value = "";
        
    }
    

function cargadatos() {
    
    let endpoint = '/controller/Cuser';
    
    alert("entro")    
    axios.get(endpoint, )
      .then(function (response) {
       let data = response.data;
       let tbody = document.getElementById("tcuerpo");    
        
       let tope = (Object.keys(data).length) +1;
       let newRow = document.createElement("tr");
       let lit ='';
       
       for (let index = 1; index < tope; index++) {
        
            lit +=`<tr>
            <th scope="row">${index}</th>
            <td>${data[index].email}</td>
            <td>${data[index].fullname}</td>
            </tr>
           `; 
       }
       tbody.innerHTML =lit;
       //newRow.appendChild(newRow);

        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      })
      .finally(function () {
        // siempre sera ejecutado
      });

}