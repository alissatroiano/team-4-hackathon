$.fn.christmas = function() {
    $(this).each(function() {
      $(this).html($(this).text().split("").map(function(v, i) {
        return '<span class="christmas-' + (i % 2 == 0 ? 'gold' : 'blue') + '">' + v + '</span>';
      }).join(""));
    });
  };
  
  $(function() { 
    $('h1.christmas').christmas();
  });
  

  // Regards to https://monsterspost.com/20-codepens-to-give-christmas-mood-to-your-website/ for the code 