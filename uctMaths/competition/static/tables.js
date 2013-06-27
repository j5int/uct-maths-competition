//edit button: switch to iput mode
function show_input(id)
{
	$('#input'+id).show()	
	$('#show'+id).hide()
}

//confirmation dialog for when you click 'Delete All' in views
function drop(type)
{
	if (del){
		return confirm('Are you sure you want to permanently delete all of your registered '+type+'s?')
	}
	else {return true}
}