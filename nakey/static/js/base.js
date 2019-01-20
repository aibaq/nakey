// cart:
function onGetCartItems(){
    if(localStorage.getItem("cartItems")){
        return JSON.parse(localStorage.getItem("cartItems"))
    }
    return [];
}
function onAddToCart(item){
    let items = [];
    if(localStorage.getItem("cartItems")){
        items = JSON.parse(localStorage.getItem("cartItems"));
        console.log(items.find(i=>i.id == item.id))
        if(items.find(i=>i.id == item.id) == undefined){
            items.push(item)
        }else{
            alert("you")
        }
    }else{
        items.push(item);
    }
    localStorage.setItem("cartItems", JSON.stringify(items));
}
function onRemoveFromCart(item_id){
    console.log(item_id)
    var items = onGetCartItems();
    var index = items.findIndex(item=>item.id == item_id);
    if(index > -1){
        items.splice(index, 1);
        localStorage.setItem("cartItems", JSON.stringify(items));
    }
    console.log(items);
}
