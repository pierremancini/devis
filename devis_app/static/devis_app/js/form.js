function roundDecimal(x) {
  // https://stackoverflow.com/questions/11832914/round-to-at-most-2-decimal-places-only-if-necessary
  return Math.round((x + Number.EPSILON) * 100) / 100;
}

// Calcul total
function set_total() {
  total = 0;
  $(".sous-total").each(function() {
    sous_total = parseFloat($(this).text().replace(',','.'));
    if (!isNaN(sous_total)) {
      total += sous_total;
    }
  });
  total = roundDecimal(total);
  $("#total").text(total.toString().replace('.', ','));
  return $("#total");
}

function set_sous_total() {
  $("#grille > tbody > tr").each(function() {
    var quantity_int = parseInt($( this ).find('.quantity').val());
    var prix_float = parseFloat($( this ).find('.prix-unite').val().replace(',','.'));
    var product = quantity_int * prix_float;
    if (product !== NaN) {
      var sous_total = roundDecimal(product).toString().replace('.', ',');
      $( this ).find(".sous-total").text(sous_total);
    }
  });
}

$(document).ready(function(){

  // --- Assignation de valeurs au chargement de la page ---
  // 
  var initDevise = $("#id_devise").val();
  $(".devise-holder").text(initDevise);

  // Set initial sous-total
  set_sous_total();

  // Set initial du total
  set_total();

  // --- Code gérant les évènements après chargement de la page
  $(".tabs .tab-links a").click(function(e) {
    var currentAttrValue = jQuery(this).attr('href');
    jQuery(currentAttrValue).css('visibility', 'visible').siblings(".panel").css('visibility', 'collapse');
    jQuery(this).parent('li').addClass('is-active').siblings().removeClass('is-active');
    e.preventDefault();
  });

  $("#nouvelle-ligne").off().on('click', function(e) {

    // Todo modifier ici, attention l'erreur de typage voir ligne 
    $("#grille tbody tr:last").after(
      '<tr><td><textarea class="textarea is-small" cols="40" rows="2" type="text">Ligne de test</textarea></td>\
      <td><input class="input is-small quantity" type="text" size="8" value=""></td>\
      <td><input class="input is-small prix-unite" type="text" size="1" value=""></td>\
      <td class="sous-total"></td></tr>');

    // calcul du total
    set_total();

  });

  $("#supprimer-ligne").click(function(e) {
    $("#grille tbody tr:last").remove();

    // calcul du total
    set_total();
  });

  $("#id_devise").on("input", function(e) {
    var dInput = this.value;
    $(".devise-holder").text(dInput)
  });

  // calcul des sous-totaux et du total
  $("#grille").on("input", ".prix-unite",  function(e) {
    // Empêche la saisi au-delà des décimales
    this.value = this.value.match(/^\d+,?\d{0,2}/);
    // calcul d'un sous-total

    set_sous_total();
    // $("#grille > tbody > tr").each(sous_total);
    // set du sous-total


    // calcul du total
    set_total();
  });

  $("#grille").on("input", ".quantity", function(e) {

    // Saisi d'entiers uniquement
    this.value = this.value.match(/^\d+/);

    // scalcul d'un sous-total
    set_sous_total();
    // $("#grille > tbody > tr").each(sous_total);

    // calcul du total
    set_total();
  });

  $("#id_date_creation").datepicker();
  $("#id_date_emission").datepicker();
});

