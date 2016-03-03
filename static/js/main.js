

$(document).ready (function(){
	$("#success-alert").hide();
    $("#approve").click(function showAlert() {
		$("#success-alert").fadeTo(2000, 500).slideUp(500, function(){
		    $("#success-alert").alert('close');
		});
	});
});

function declineTaskPrompt() {

    var comment = prompt("Please enter some feedback to help Jim do a better job:", "");
    
    if (comment != null) {
        document.getElementById("comments").innerHTML =
        comment;
    }
}