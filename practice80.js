// https://www.codewars.com/kata/fun-with-lists-trees-edition/javascript

function flatten(head) {
    if (head === null){
      return null;
    }

    function getValFromTree(t){
      if (t instanceof TreeNode){
        return [t.value].concat(getValFromTree(t.left).concat(getValFromTree(t.right)));
      }
      return [];
    }
    let curr = head;
    let data = [];
    while (curr != null){
      data = data.concat(getValFromTree(curr.data));
      curr = curr.next;
    }
    data = Array.from(new Set(data)).sort(function(a, b) {
      return a - b;
    });

    let resultList = new ListNode(new TreeNode(data[0], null, null));
    let idx = 1;
    let currNode = resultList;
    let lastNode = resultList;
    while (idx < data.length){
      let newTreeNode = new TreeNode(data[idx], null, null);
      idx += 1;
      lastNode.next = new ListNode(newTreeNode);
      lastNode = lastNode.next;

      if (currNode.data.left === null){
        currNode.data.left = newTreeNode;
      } else {
        currNode.data.right = newTreeNode;
        currNode = currNode.next;
      }
    }

    return resultList.data;
  };