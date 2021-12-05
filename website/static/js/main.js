/*
	* cette fonction change letat du checkbox 
		- en ajoutant l'attribut checked 
*/ 
function set_checkbox()
{
	let checkbox = document.querySelector("#available");
	let check = checkbox.getAttribute('value');

	if (check == 'True')
	{
		checkbox.setAttribute("checked" , "checked")
	}

	// console.log(check)
}

// function background_404()
// {
// }