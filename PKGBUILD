# Maintainer: siphr <archlinux@techtum.dev>
pkgname=aur-info
pkgver=0.2
pkgrel=1
pkgdesc="Retrieve package info for an aur package."
depends=(python)
arch=(x86_64)
source=("https://github.com/siphr/urdu.git")
license=('MIT')

build() {
    pip install urdu -U
    pip install bs4 -U
    
    echo "echo `date`" > aur-info
    echo "python -m urdu \$@" >> aur-info

    chmod +x $srcdir/urdu
}

package() {
    mkdir -p $pkgdir/usr/bin
#    echo $srcdir
    cp "$srcdir/aur-info" "$pkgdir/usr/bin/aur-info"
    echo 'Finsihed setting up aur-info.'
}
