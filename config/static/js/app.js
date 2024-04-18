
function saludar() {
    let email = document.getElementById("exampleInputEmail1")
    alert("Hola Mundo "+ email.value);
}
/***
 * <tr>
        <th scope="row">1</th>
        <td>Mark</td>
        <td>Otto</td>
        <td>@mdo</td>
      </tr>
 */
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
    