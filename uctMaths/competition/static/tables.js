function toggle_input(id, type)
{
	$('#show'+id).toggle()
	$('#ask'+id).toggle()
	// alert(id)
	// alert("in function")
	if(type=="ask"){
		// $(this).parent().innerHTML = "edit"
		$('#button'+id).attr('value','edit')
		// alert(id)
	}
	else if (type=='show'){
		$('#button'+id).attr('value','undo')
		// alert(id)
	}
}