if !haskey(Pkg.installed(), "LatBo")
    Pkg.clone("git@github.com:UCL/LatBo.jl.git", "close_enough")
end