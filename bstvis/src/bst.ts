export class Node {
  value: number;
  left: Node | undefined;
  right: Node | undefined;

  constructor(value: number) {
    this.value = value;
  }

  insert(value: number): undefined {
    if (this.value == value) {
      return;
    }
    if (value < this.value) {
      if (this.left !== undefined) {
        return this.left.insert(value);
      }
      this.left = new Node(value);
    } else {
      if (this.right !== undefined) {
        return this.right.insert(value);
      }
      this.right = new Node(value);
    }
  }

  find(value: number): boolean {
    if (this.value == value) {
      return true;
    }
    return Boolean(this.left?.find(value) || this.right?.find(value))
  }

  sizeRec(): number {
    return 1 + (this.left?.sizeRec() || 0) + (this.right?.sizeRec() || 0)
  }

  menorRec(): number {
    return this.left !== undefined ? this.left.menorRec() : this.value
  }

  maiorRec(): number {
    return this.right !== undefined ? this.right.maiorRec() : this.value
  }

  alturaRec(): number {
    return Math.max(this.left !== undefined ? 1 + this.left.alturaRec() : 0, this.right !== undefined ? 1 + this.right.alturaRec() : 0)
  }

  internalPathLenghtRec(depth: number): number {
    return depth + (this.left?.internalPathLenghtRec(depth + 1) || 0) + (this.right?.internalPathLenghtRec(depth + 1) || 0)
  }

  preOrdem(l: number[]): undefined {
    l.push(this.value)
    if (this.left !== undefined)
      this.left.preOrdem(l)
    if (this.right !== undefined)
      this.right.preOrdem(l)
  }

  posOrdem(l: number[]): undefined {
    if (this.left !== undefined)
      this.left.posOrdem(l)
    if (this.right !== undefined)
      this.right.posOrdem(l)
    l.push(this.value)
  }

  emOrdem(l: number[]): undefined {
    if (this.left !== undefined)
      this.left.emOrdem(l)
    l.push(this.value)
    if (this.right !== undefined)
      this.right.emOrdem(l)
  }
}

export class BST {
  root: Node | undefined;

  push(value: number) {
    if (this.root == undefined) {
      this.root = new Node(value);
    }
    this.root.insert(value);
  }

  find(value: number): boolean {
    if (this.root === undefined) {
      return false
    }
    return this.root.find(value)
  }

  size(): number {
    if (this.root === undefined) {
      return 0
    }
    return this.root.sizeRec()
  }

  min(): number | unknown {
    return this.root?.menorRec()
  }

  max(): number | unknown {
    return this.root?.maiorRec()
  }

  height(): number {
    if (this.root === undefined) {
      return 0
    }
    return this.root.alturaRec()
  }

  internalPathLength(): number {
    if (this.root === undefined) {
      return 0
    }
    return this.root.internalPathLenghtRec(0)
  }

  preOrdem(): number[] {
    const l: number[] = []
    if (this.root !== undefined) {
      this.root.preOrdem(l)
    }
    return l
  }

  posOrdem(): number[] {
    const l: number[] = []
    if (this.root !== undefined) {
      this.root.posOrdem(l)
    }
    return l
  }

  emOrdem(): number[] {
    const l: number[] = []
    if (this.root !== undefined) {
      this.root.emOrdem(l)
    }
    return l
  }

  levelOrder(): number[] {
    const l: number[] = []
    let fila: Node[] = []
    let emEspera: Node[] = []
    if (this.root !== undefined) {
      emEspera.push(this.root)
    }
    while (emEspera.length > 0) {
      fila = emEspera.sort((a,b) => b.value - a.value)
      emEspera = []
      while (fila.length > 0) {
        const n = fila.pop()
        l.push(n!.value)
        if (n?.right !== undefined)
          emEspera.push(n.right)
        if (n?.left !== undefined)
          emEspera.push(n.left)
      }
    }
    return l
  }
}
