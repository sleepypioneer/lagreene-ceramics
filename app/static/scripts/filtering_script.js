// Initialize GLightbox when DOM is ready
var lightbox = null;

document.addEventListener('DOMContentLoaded', function() {
    lightbox = GLightbox({
        selector: '.glightbox'
    });
});

function showItem(item) {
    item.classList.remove('d-none');
    item.classList.add('fadeIn', 'glightbox');
}

function hideItem(item) {
    item.classList.add('d-none');
    item.classList.remove('fadeIn', 'glightbox');
}

function clean() {
    const items = Array.from(document.getElementsByClassName("filter"));
    items.map(function (item, index) {
        item.classList.remove('fadeIn');
    });
}

function removeSelection() {
    const selected = document.getElementsByClassName('selected');
    if (selected.length > 0) {
        for (let i = 0; i < selected.length; i++) {
            selected[i].classList.remove('selected');
        }
    }
}

function setSelected(id) {
    removeSelection();
    const selector = document.getElementById(id);
    selector.classList.add('selected');
}

function filterGallery(id, classes) {
    setSelected(id)
    const items = Array.from(document.getElementsByClassName("filter"));
    const videoSection = document.getElementById("gallery-videos");
    const galleryContainer = document.getElementById("gallery-container");

    // Handle videos filter
    if (id === "video_section") {
        videoSection.classList.remove('d-none');
        galleryContainer.classList.add('d-none');
        return;
    } else {
        videoSection.classList.add('d-none');
        galleryContainer.classList.remove('d-none');
    }

    items.map(function (item, index) {
        const itemContainsClass = item.classList.contains(id);
        switch (id) {
            case "all":
                if (item.classList.contains('archive')) {
                    hideItem(item);
                } else {
                    showItem(item);
                }
                setTimeout(clean, 500);
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

    // Reinitialize GLightbox after filtering to pick up DOM changes
    if (lightbox) {
        lightbox.destroy();
    }
    lightbox = GLightbox({
        selector: '.glightbox'
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