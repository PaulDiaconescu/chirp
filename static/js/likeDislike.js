/**
 * Created by P5RO-PORT079 on 7/26/2017.
 */

(function(){
    'use strict';
    $(document).ready(function(){
        $('.like-message').click(function(){
            alert("Pressed a like button!");
            var request = $.ajax({
                url: "http://127.0.0.1:8000/like/",
                method: "POST",
                data: {id : "SUNT ID!"}
            });

            request.done(function(){
               alert("SUCCES!");
            });

            request.fail(function(){
                alert("FAIL!");
            });

        });
        $('.dislike-message').click(function(){
            alert("Pressed a dislike button!");
        });
    });
})();
