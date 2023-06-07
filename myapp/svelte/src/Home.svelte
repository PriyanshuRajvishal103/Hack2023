<script>
alert("heelo world");
</script>

<body>
    <div class="header">
        <h1 id ="h1"class="hh">Welcome to Booking platform</h1>
        <div id ="h2"class="hh"></div>
        <div id ="h3"class="hh">
           <div class="logparent">

           <div class="log login"></div>
            <div class="log signin"></div>
           </div>
         </div>
    </div>
    <div class="fromto">
        <div class="p p1">
            <div class="q q1">
                
               
                
            </div>
            <div class="q q2"></div>
        </div>
        <div class="change"></div>
        <div class="p p2"></div>
    </div>
</body>

<style>

*{
            margin: 0%;
            padding:0px;
        }
       body{
        height: 100vh;
        width: 100vw;
        background-color: rgb(12, 133, 147);
       }
       .header{
        height: 10vh;
        width: 99.8vw;
        border: 2px solid red;
       }
       .hh{
        height: 90%;
        display: inline-block;
        border: 1px solid;
        width: 100%;
       }
       #h1{
        width: 20vw;
       }
       #h2{
        width: 55vw;
       }
       #h3{
        width: 23vw;
        margin-top: 0px;
       }
        @media only screen and (max-width: 480px) {
            body{
              background-color: lightgreen;
            }
          .header{
            height: 70px;
          }
            #h1{
              
                width: 70px;
            }
            #h2{
                width: 230px;
            }
            #h3{
                width: 70px;
                margin-top: 0px;
            }
          }
        
        .logparent{
            height: 100%;
            width: 100%;
            background-color: black;
        }
        .log{
            height: 20px;
            width: 110px;
            margin-top: 10px;
            background-color: aliceblue;
            display: inline;
        }

        .fromto{
            height:40vh ;
            width: 80vw;
            border: 1px solid yellow;
            margin-left: 8%;
            margin-top: 10vh;
        }
        .p{
            height: 90%;
            width: 45%;
            border: 1px solid white;
            display: inline-block;
            margin: 9px 23px;
            background-color: pink;

        }
        .change{
            display: none;
        }
        .q{
            height: 30%;
            width: 90%;
            border: 1px solid black;
            
        }
        .q1{
            margin-top: 15px;
            margin-left: 20px;
        }
        .q2{
            margin-top: 20px  ;
            margin-left: 50px;
        }
        .s{
            height: 80%;
            width: 20%;
          
            border: 1px solid black;
        }
        .se{
            height: 10px;
            width: 20px;
            border:1px solid red;
        }
        @media only screen and (max-width: 480px){
            .fromto{
                height: 100px;
                width: 350px ;
            }
            .p{
                height: 90%;
                width: 35%;
                border: 1px solid white;
                display: inline-block;
                margin: 4px 2px;
            }
            .change{
                display: inline-block;
                height: 40%;
                width: 20%;

                border: 1px solid red;
                margin-bottom: 25px;
            }
            .q{
                display: none;
            }
           

        }
</style>