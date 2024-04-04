<script>
    import { goto } from '$app/navigation';
    import AkarIconsEdit from '~icons/akar-icons/edit';

    function openCustomisePressed() {
        goto("/customise");
    }
</script>

<div>
    <button on:click={openCustomisePressed}/>
    <AkarIconsEdit style='position: absolute; margin-top: 20px; margin-left: 25px; width: 30px; height: 30px;'/>
    <p style='margin-left: 80px; margin-top: 25px;'>Customise</p>
    <p id="plus">+</p>
</div>

<style>
    div #plus {
        text-align: center;
        margin-top: 60px;
        font-size: 50px;
    }

    div {
       
        border-radius: 8px;
        background-color: #EDEDED;
        cursor: pointer;
        border: none;
        font-family:'Franklin Gothic Light';
    }

    p {
        font-size: large;
        margin-left: 20px;
    }

    div button {
        position: absolute;
        width: 400px;
        height: 225px;
        border-radius: 10px;
        background-color: transparent;
        cursor: pointer;
        border: none;    
    }
</style>