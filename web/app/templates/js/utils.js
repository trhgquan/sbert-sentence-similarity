/**
 * Generating code template for result.
 * @param {Object} response_dict 
 * @returns String
 */
 function generate_template(response_dict) {
    let result_display = '';

    result_display += "<div class='accordion' id='accordion_template'>";
    
    Object.entries(response_dict).map(([id, dict]) => {
        result_display += "<div class='accordion-item'>";
        result_display += "<h2 class='accordion-header' id='accordion_heading_" + id + "'>";
        result_display += "<button class='accordion-button collapsed'" +
            " type='button' data-bs-toggle='collapse' data-bs-target='#accordion_collapse_" + id + "'" +
            " aria-expanded='false' aria-controls='accordion_heading_" + id + "'>";
        result_display += "<b>";
        result_display += dict.sentence;
        result_display += "</b>";
        result_display += "</button>"
        result_display += "</h2>";
    
        result_display += "<div id='accordion_collapse_" + id + "' class='accordion-collapse collapse'" +
            " aria-labeledby='accordion_heading_" + id + "' data-bs-parent='#accordion-template'>";
        
        result_display += "<div class='accordion-body'>"
        result_display += "<p>";
        result_display += "Similarity score: ";
        result_display += dict.score;
        result_display += "</p>";

        result_display += "<p>";
        result_display += "Verdict: ";
        result_display += (dict.similar) ? "<span class='badge bg-success'>" : "<span class='badge bg-danger'>";
        result_display += (dict.similar) ? "Similar" : "Not similar";
        result_display += "</span>";
        result_display += "</p>";

        result_display += "</div>";
        result_display += "</div>";
        result_display += "</div>";
    });
    
    result_display += "</div>";

    return result_display;
}

export default generate_template;