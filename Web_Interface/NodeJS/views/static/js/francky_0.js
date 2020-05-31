<script type="text/javascript" charset="utf-8">
    $(document).ready(function(){
        var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
        // verify our websocket connection is established
        socket.on('connect', function() {
        console.log('Websocket connected!');
        });

        socket.on('my_horloge', function(msg){
        console.log('Test my_horloge');
        console.log(msg);
        });

        /*socket.on('my_horloge', function(msg) {
        $('#system_time').replace(msg.data);
        console.log(msg.data);
           });*/

    });
    </script>