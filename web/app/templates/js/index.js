$("#submit_scoring").on("click", function() {
    // Disabling submit button to prevent spamming
    $("#submit_scoring").attr("disabled", true);

    // Remove all errors
    $('form').find('.is-invalid').each(function() {
        $(this).removeClass('is-invalid');
    });

    // Get input sentences
    let target_sentence = $("#target_sentence").val();
    let sentences_list = $("#sentences_list").val();

    // Get and scale threshold to range [0, 1]
    let threshold_max = $("#threshold_max").val();
    threshold_max = threshold_max / 100;

    // Send request to API.
    let request = $.ajax({
        url : "{{ url_for('score') }}",
        type : "POST",
        data : {
            "target_sentence" : target_sentence,
            "sentences_list" : sentences_list,
            "threshold_max" : threshold_max
        }
    })

    // If the request is success
    request.done(function(response, textStatus, jqXHR) {
        console.log(response)
    });

    // When the request failed (aka nothing to predict)
    // this will set an error class to that field.
    request.fail(function(jqXHR, textStatus, errorThrown) {
        let error_field = JSON.parse(jqXHR.responseText).error_field;

        $("#" + error_field).addClass('is-invalid');
    });

    // Enable submit button after finished.
    request.always(function() {
        $("#submit_scoring").attr("disabled", false);
    });
});

$("#threshold_max").on("change", function() {
    // Empty current threshold field
    $("#current_threshold").text();

    // Get current threshold and scale it to range [0, 1], then set to the field above.
    let current_threshold = $("#threshold_max").val();
    $("#current_threshold").text(current_threshold / 100);
});