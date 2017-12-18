
function typeInput () {

	let input = getId ( 'searcher-input' );

	let wallet_default = /^xrb_/;
	let block_default = /[A-Z]|[0-9]/;

	if ( wallet_default.test ( input.value ) ) {
		$( '.mdl-button' ) .disabled = false;
		$( '.searcher' ) .action = "/wallet";
		input.name = "w";

	} else if ( block_default.test ( input.value ) && input.value.length == 64 ) {
		$( '.mdl-button' ) .disabled = false;
		$( '.searcher' ) .action = "/block";
		input.name = "b";

	} else {
		$( '.mdl-button' ) .disabled = true;
		$( '.searcher' ) .action = "";
		input.name = "";
	}
}
