
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
    let email = document.getElementById("exampleInputEmail1")
    let fullname = document.getElementById("FullName")
    let tcuerpo = document.getElementById("tcuerpo")
    let data ='';
    data = '<tr>';
    data += '<th scope="row">1</th>';
    data += '<td>'+email.value+'</td>';
    data += '<td>'+fullname.value+'</td>';
    data += '</tr>';
    tcuerpo.innerHTML = data;
}