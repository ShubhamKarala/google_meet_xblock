function GoogleMeetXBlock(runtime, element) {
    // Additional JavaScript if needed
}

function GoogleMeetXBlockStudio(runtime, element) {
    $('#save-meet-url', element).click(function() {
        const meetUrl = $('#meet-url-input', element).val();
        runtime.notify('save', {state: 'start'});
        runtime.ajax('save_meet_url', {meet_url: meetUrl})
            .done(function(response) {
                runtime.notify('save', {state: 'end'});
                alert("Google Meet URL saved!");
            });
    });
}
