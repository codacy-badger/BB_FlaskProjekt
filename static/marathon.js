function deleteLaufer(button)
{
    if(window.confirm("Wollen Sie das Item wirklich löschen"))
    {
        button.form.submit();
    }
}