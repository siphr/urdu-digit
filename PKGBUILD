# Maintainer: siphr <archlinux@techtum.dev>
pkgname=urdu-digit
pkgver=0.2
pkgrel=1
pkgdesc="Retrieve package info for an aur package."
depends=(python)
arch=(x86_64)
source=("https://github.com/siphr/urdu-digit.git")
license=('MIT')

build() {
    pip install urdu-digit -U
    pip install bs4 -U
    
    echo "echo `date`" > urdu-digit 
    echo "python -m urdu_digit \$@" >> urdu-digit

    chmod +x $srcdir/urdu-digit
}

package() {
    mkdir -p $pkgdir/usr/bin
#    echo $srcdir
    cp "$srcdir/urdu-digit" "$pkgdir/usr/bin/urdu-digit"
    echo 'Finsihed setting up urdu-digit.'
}
