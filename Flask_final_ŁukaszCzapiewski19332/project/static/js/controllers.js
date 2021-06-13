var portfolioApp = angular.module('portfolioApp', []);
portfolioApp.controller('GalleryListCtrl', function ($scope) {
    $scope.galleries = [
        {   
            'section': 'Kolumna 1',
            'title': 'Astronaut Teemo',
            'when': '2010-10-27',
            'thumbnailUrl': 'img/astronaut.jpg'
        },
        {   
            'section': 'Kolumna 2',
            'title': 'Happy Elf Teemo',
            'when': '2009-12-16',
            'thumbnailUrl': 'img/elf.jpg'
        },
        {   
            'section': 'Kolumna 1',
            'title': 'Super Teemo',
            'when': '2011-10-10',
            'thumbnailUrl': 'img/hero.jpg'
        },
        {   
            'section': 'Kolumna 2',
            'title': 'Omega Squad Teemo',
            'when': '2015-04-09',
            'thumbnailUrl': 'img/squad.jpg'
        },
        {   
            'section': 'Kolumna 1',
            'title': 'Panda Teemo',
            'when': '2012-07-09',
            'thumbnailUrl': 'img/panda.jpg'
        },
        {   
            'section': 'Kolumna 2',
            'title': 'Cottontail Teemo',
            'when': '2011-04-19',
            'thumbnailUrl': 'img/krolik.jpg'
        }
    ];
});


