$(document).ready( function () {
    $('#bsborders_table').DataTable({
        dom: 'Blfrtip',
        lengthMenu: [
            [ 10, 25, 50, -1 ],
            [ '10 rows', '25 rows', '50 rows', 'Show all' ]
        ],
        buttons: [
             'copy', 'csv', 'pdf', 'print'
        ]
    } );
} );