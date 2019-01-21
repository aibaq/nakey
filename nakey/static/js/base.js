// cart:
function onGetCartItems(){
    if(localStorage.getItem("cartItems")){
        return JSON.parse(localStorage.getItem("cartItems"))
    }
    return [];
}
function onUpdateCartItems(items){
    localStorage.setItem("cartItems", JSON.stringify(items));
}
function onAddToCart(item){
    let items = [];
    item.count = 1;//default count is 1;
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
    onUpdateCartItems(items)
}
function onRemoveFromCart(item_id){
    console.log(item_id)
    var items = onGetCartItems();
    var index = items.findIndex(item=>item.id == item_id);
    if(index > -1){
        items.splice(index, 1);
        onUpdateCartItems(items)
    }
    console.log(items);
}
function onUpdateCartItem(item_id, newcount){
    items = onGetCartItems();
    console.log("Update", items, item_id, newcount)
    var searchitem = items.find(item=>{ return item.id == item_id; });
    console.log("search", searchitem)
    if(searchitem != undefined){
        searchitem.count = newcount;
        onUpdateCartItems(items)
    }
}
