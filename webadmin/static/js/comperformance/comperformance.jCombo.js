;(function( $, window, document, undefined ) {

    $(document).ready(function() {
        $("#studentaddclass").jCombo("/ajax/select_classes/",{
            initial_text:'-- Please Select --',
        });

        $("#editstudentaddclass").jCombo("/ajax/select_classes/",{
            initial_text:'-- Please Select --',
        });
    });

}) (jQuery, window, document);
