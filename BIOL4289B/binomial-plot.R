p <- seq(0, 1, length.out=20)
y <- 0:20
z <- sapply(p, function(p.val) {
  sapply(y, function(h) dbinom(h, 20, p.val))
})

require(lattice)
levelplot(z)

require(rgl)

x <- 0.1*(1:nrow(z))
y <- 0.1*(1:ncol(z))
zlim <- range(y)
zlen <- zlim[2]-zlim[1]+1

open3d(); surface3d(x, y, z, front='fill', back='lines', color=terrain.colors(zlen))
rgl.snapshot('persp.png')
