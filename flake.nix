{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = (import nixpkgs {
        inherit system;
      });
    in {
      devShells.${system}.default = pkgs.mkShell {
        nativeBuildInputs = with pkgs; [ clang-tools cmake ];
        buildInputs = with pkgs; [
          gcc
          gdb
          valgrind
          (python313.withPackages (p: with p; [
            matplotlib
          ]))
          basedpyright
        ];
        shellHook = ''
          function run_cpp {
            outDir="`dirname $(realpath $1)`/bin"
            mkdir -p "$outDir"
            g++ -std=gnu++17 -Wall -ggdb "$1" -o ''${outDir}/''${1%.cpp}.out
            ''${outDir}/''${1%.cpp}.out
          }
        '';
      };
    };
}
