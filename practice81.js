// https://www.codewars.com/kata/fun-with-trees-lists-edition/javascript

function flatten(root) {

    function getValsFromTreeNode(node){
      let listVals = [];
      let currNode = node.value;
      while (currNode){
        listVals.push(currNode.data);
        currNode = currNode.next;
      }
      return listVals;
    }

    function getValsFromTree(node){
      if (node === null){
        return [];
      }
      let nodeVals = getValsFromTreeNode(node);

      if (node.left != null){
        nodeVals = nodeVals.concat(getValsFromTree(node.left));
      }
      if (node.right != null){
        nodeVals = nodeVals.concat(getValsFromTree(node.right));
      }
      return nodeVals;
    }
    let allVals = Array.from(new Set(getValsFromTree(root))).sort(function(a, b) {
        return a - b;
      });

    if (allVals.length === 0){
      return null;
    }

    let resultList = new ListNode(allVals[0]);
    let currNode = resultList;
    for (let idx = 1; idx < allVals.length; idx++){
      currNode.next = new ListNode(allVals[idx]);
      currNode = currNode.next;
    }
    return resultList;
  };