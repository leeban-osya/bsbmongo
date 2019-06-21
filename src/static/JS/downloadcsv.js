$(document).ready(function() {

  $('table').each(function() {
    var $table = $(this);
    var $button = $("<button type='button'>");
    $button.text("Export results to CSV");
    $button.insertBefore($table);

    $button.click(function() {
        var csv = $table.table2csv({delivery:'value'});

    });
  });
});