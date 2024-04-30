<script>
    import FaUserCircle from '~icons/fa/user-circle';
</script>


<div id="navbar">
    <FaUserCircle style='position: absolute; width: 40px; height: 40px; margin-left: 35px; margin-top: 40px;'/>
    <p style = 'font-size: 20px;'><b>Username Here</b></p>
    <button id="logout">Logout</button>
    <button id="profile">Profile</button>
    <div id="navbar-content">
    </div>
</div>

<style>
    #logout {
        margin-top: 60px; 
        margin-left: 100px; 
        border-radius: 4px;
        border: none;
        width: 60px;
        height: 25px;
        background-color: #DA0037;
    }

    #profile {
        width: 60px;
        height: 25px;
        border-radius: 4px;     
        background-color: #757272;
        border: none;
    }


    #navbar-content {
        display: flex;
        flex-direction: column;
       
        margin-top: 25px;
      
        
    }

    #navbar {
       
        width: 100%; 
        height: flex;
        background-color: #EDEDED;
        margin: 0;
        box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
       
    }

    #navbar p {
        position: absolute;
        margin-left: 100px;
        margin-top: 35px;
        margin-bottom: 35px;
        font-family: 'Century751-Roman';
    }
</style>