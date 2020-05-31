let lightbox = GLightbox({
    selector: 'glightbox',
    touchNavigation: true,
    onOpen: () => {
      console.log('Lightbox opened')
    },
});

const showItem = (item) => {
    item.classList.remove('d-none');
    item.classList.add('fadeIn','glightbox');
  }

const hideItem = (item) => {
    item.classList.add('d-none');
    item.classList.remove('fadeIn','glightbox');
}

const clean = () => {
    const items = Array.from(document.getElementsByClassName("filter"));
    items.map(function (item, index) {
        item.classList.remove('fadeIn');
    })
}

const removeSelection = () => {
    selected = document.getElementsByClassName('selected')
    if(selected.length > 0) {
        for (i=0; i < selected.length; i++) {
            selected[i].classList.remove('selected');
        }
    }
}

const setSelected = (id) => {
    removeSelection();
    const selector = document.getElementById(id);
    selector.classList.add('selected')
}

function filterGallery(id, classes) {
    setSelected(id)
    const items = Array.from(document.getElementsByClassName("filter"));
    items.map(function (item, index) {
        const itemContainsClass = item.classList.contains(id);
        switch(id) {
            case "all":
                if (item.classList.contains('archive')){
                    hideItem(item);
                } else {
                    showItem(item);
                }
                setTimeout(clean,500);
                break;
            case "archive":
                if (itemContainsClass) {
                    showItem(item);
                } else {
                    hideItem(item);
                }
                break;
            default:
                if (itemContainsClass && !item.classList.contains('archive')) {
                    showItem(item);
                } else {
                    hideItem(item);
                }
        }
    })
    lightbox = GLightbox({
        selector: 'glightbox',
        touchNavigation: true,
        onOpen: () => {
          console.log('Lightbox opened')
        },
    });
}

function filterStockists(id) {
    const items = Array.from(document.getElementsByClassName("filter"));
    items.map(function (item, index) {
        const check = item.classList.contains(id);
        if (check && !item.classList.contains('archive')) {
            item.classList.remove('d-none');
            item.classList.add('d-flex');
        } else {
            item.classList.add('d-none');
            item.classList.remove('d-flex');
        }
    })
}