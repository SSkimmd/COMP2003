<script>
    // @ts-ignore
    import { goto } from '$app/navigation';
    import AkarIconsEdit from '~icons/akar-icons/edit';

    function openCustomisePressed() {
        goto("/customise");
    }
/**
     * Function to prevent the button click event from bubbling up to the parent div
     * and triggering its click event.
     * @param {Event} event The click event
     */
     function stopPropagation(event) {
        event.stopPropagation();
    }
    
</script>

<div style='border-radius: 8px; cursor: pointer; position: relative;'>
    <button on:click={openCustomisePressed} on:click|preventDefault={stopPropagation} />
    <AkarIconsEdit style='position: absolute; margin-top: 20px; margin-left: 25px; width: 30px; height: 30px;'/>
    <p style='margin-left: 80px; margin-top: 20px; font-size: 24px;'><b>Customise</b></p>
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
        font-family:'Century751-Roman';
        box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
        transition: filter 0.7s ease;
    }

    div:hover {
        filter: brightness(90%);
    }
        
    

    p {
        font-size: large;
        margin-left: 20px;
    }

    div button {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        background-color: transparent;
        border: none;
        cursor: pointer;
        z-index: 1;
    }

   
</style>
