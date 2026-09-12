class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const sm=new Map();
        const tm=new Map();
        for(let i of s){
            if(i in sm){
                sm[i]+=1
            }else{
                sm[i]=1
            }
        }
        for(let i of t){
            if(i in tm){
                tm[i]+=1
            }else{
                tm[i]=1
            }
        }
        if(Object.keys(sm).length!=Object.keys(tm).length){
            return false
        }
        for(let key in sm){
            if(sm[key]!==tm[key]){
                return false
            }
        }
        return true
    }
}
