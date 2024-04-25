<script>
    import FaUserCircle from '~icons/fa/user-circle';
</script>


<div id="navbar">
    <FaUserCircle style='position: absolute; width: 40px; height: 40px; margin-left: 35px; margin-top: 40px'/>
    <p>Username Here</p>
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
        background-color: #444444;
        border: none;
    }


    #navbar-content {
        display: flex;
        flex-direction: column;
       
        margin-top: 25px;
      
        
    }

    #navbar {
       
        width: flex; 
        height: flex;
        background-color: #EDEDED;
        
       
    }

    #navbar p {
        position: absolute;
        margin-left: 100px;
        margin-top: 35px;
        margin-bottom: 35px;
        font-family: 'Franklin Gothic Light';
    }
</style>