
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
    
       
        let email = emailInput.value;
        let fullname = fullnameInput.value;
    
        
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
    