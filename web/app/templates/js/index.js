import generate_template from './utils.js';

$("#submit_scoring_btn").on("click", function() {
    // Disabling buttons to prevent spamming
    $('#btn_zone > button').each((_item, button) => {
        $(button).attr("disabled", true);
    });

    // Update submit button spinner & text.
    $("#submit_scoring_btn_spinner").removeClass("visually-hidden");
    $("#submit_scoring_btn_text").text("Calculating similarity scores..");

    // Clear output zone
    $("#result_display").html("Will be here when all processings are done.");

    // Remove all errors
    $("form").find(".is-invalid").each(function() {
        $(this).removeClass("is-invalid");
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
    request.done((response, _textStatus, _jqXHR) => {
        let result_display = generate_template(response.response_dict);

        $("#result_display").html(result_display);
    });

    // When the request failed (aka nothing to predict)
    // this will set an error class to that field.
    request.fail((jqXHR, _textStatus, _errorThrown) => {
        let error_field = JSON.parse(jqXHR.responseText).error_field;

        $("#" + error_field).addClass("is-invalid");
    });

    request.always(() => {
        // Enable submit button after finished.
        $('#btn_zone > button').each((_item, button) => {
            $(button).attr("disabled", false);
        });

        // Hide submit spinner & update its text.
        $("#submit_scoring_btn_spinner").addClass("visually-hidden");
        $("#submit_scoring_btn_text").text("Calculate similarity scores");
    });
});

$("#threshold_max").on("input", function() {
    // Empty current threshold field
    $("#current_threshold").text();

    // Get current threshold and scale it to range [0, 1], then set to the field above.
    let current_threshold = $("#threshold_max").val();
    $("#current_threshold").text(current_threshold / 100);
});