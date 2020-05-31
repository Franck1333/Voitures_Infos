function update_values() {
            $.get("/",out).done(
                function(data) {
                    $("#system_time").text(data.system_time)
                });
        }