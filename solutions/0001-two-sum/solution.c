/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    // 1. Correctly set the return size using the pointer
    *returnSize = 2; 
    
    int *arr = (int*) malloc(2 * sizeof(int));

    for(int i = 0; i < numsSize; i++) {
        // 2. Start j at i + 1 to avoid using the same element twice
        for(int j = i + 1; j < numsSize; j++) {
            if(nums[i] + nums[j] == target) {
                arr[0] = i;
                arr[1] = j;
                // 3. Return immediately once found
                return arr; 
            }
        }
    }
    
    // Safety return if no solution is found
    return NULL; 
}

