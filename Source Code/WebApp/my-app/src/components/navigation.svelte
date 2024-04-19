<script>
    import FaUserCircle from '~icons/fa/user-circle';
    import { goto } from '$app/navigation';

    function openLogoutPressed() {
        goto("/");
    }

    function openProfilePressed() {
        goto("/profile");
    }
</script>


<div id="navbar">
    <FaUserCircle style='position: absolute; width: 40px; height: 40px; margin-left: 35px; margin-top: 40px'/>
    <p>Username Here</p>
    <button id="logout" on:click={openLogoutPressed}>Logout</button>
    <button id="profile" on:click={openProfilePressed}>Profile</button>
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
        width: 100%;
        margin-top: 100px;
        margin-left: 30px;
    }

    #navbar {
        position: absolute;
        width: 300px; 
        height: 75vh;
        background-color: #EDEDED;
        border-radius: 8px;
        margin-left: 50px;
    }

    #navbar p {
        position: absolute;
        margin-left: 100px;
        margin-top: 35px;
        font-family: 'Franklin Gothic Light';
    }
</style>