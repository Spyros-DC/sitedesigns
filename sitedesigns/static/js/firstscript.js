$(document).ready(function() {
	
	$('.tabs a').click(function() {
		// save $(this) in a variable for efficiency
		var $this = $(this);
		
		// hide panels
		$('.panel').hide();
		$('.tabs a.active').removeClass('active');
		    
		// add active state to new tab
		$this.addClass('active').blur();	
		// retrieve href from link (is id of panel to display)
		var panel = $this.attr('href');

		// show panel
		$(panel).fadeIn(250);
		
		// don't follow link down page
		return(false);
	}); // end click



$('.tabs li:first a').click();
 	

//Εδώ αρχίζει το δικό μου μέρος
var var1;
var var2;
var var3;
var logo = $('.logo');

function one(){
var1 = setTimeout(function() {
    	logo.css('background-position','0px -100px');}, 1500);
}
function two(){
var2 = setTimeout(function() {
    	logo.css('background-position','-300px -100px');}, 1500);
}
function three() {
var3 = setTimeout(function() {
    	logo.css('background-position','-600px -100px');}, 1500);
}

one();


$('a#one').click(function (){
	logo.css('background-position', '0px 0px');
	one();
	clearTimeout(var2);
	clearTimeout(var3);
});
$('a#two').click(function (){
	logo.css('background-position', '-300px 0px');
	two();
	clearTimeout(var1);
	clearTimeout(var3);
});
$('a#three').click(function (){
	logo.css('background-position', '-600px 0px');
	three();
	clearTimeout(var1);
	clearTimeout(var2);
});


}); // end ready
