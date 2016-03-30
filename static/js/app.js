/**
 * Created by my on 16/3/23.
 */
$(document).ready(function () {

    //        密码不一致
    $("#password_confirm").blur(function () {
        if ($("#password_confirm").val() != $("#password").val()) {
            $("#password_confirm ").css("border","2px solid red");
        }
        else {
            $("#password_confirm ").css("border","1px solid #5bc0de");
        }
    })

    //邮箱格式不对
    $("#email").blur(function(){
        var reg = /^([\.a-zA-Z0-9_-])+@([a-z-Z0-9_-])+(\.[a-zA-Z0-9_-])+/;
        var str = $("#email").val();
        if(str!=''){
            if(!reg.test(str)){
//                        $("#email").addClass("has-error");
//                        alert("hello");
                $("#email").css("border","2px solid red");
            }
            else {
                $("#email").css("border","1px solid #5bc0de");
            }
        }

    })
})