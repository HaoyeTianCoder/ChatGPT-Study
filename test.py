import pickle
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

def calculate_distribution2():
    with open('./explanation_vectors.pickle', 'rb') as f:
        explanation_vectors = pickle.load(f)
    with open('./description_vectors.pickle', 'rb') as f:
        description_vectors = pickle.load(f)

    result = []
    for k,v in explanation_vectors.items():
        print('question: {}'.format(k))
        des_vector = description_vectors[int(k)-1]

        correct_vectors = v['correct']
        print('correct:')
        for i in range(len(correct_vectors)):
            sim = cosine_similarity(correct_vectors[i][1].reshape(1, -1), des_vector.reshape(1, -1))
            result.append([k, 'Correct', correct_vectors[i][0], sim[0][0]])

        # print('correct similarity: {}'.format(np.array(result[k][0]).mean()))
        wrong_vectors = v['wrong']
        print('wrong:')
        for i in range(len(wrong_vectors)):
            sim = cosine_similarity(wrong_vectors[i][1].reshape(1, -1), des_vector.reshape(1, -1))
            result.append([k, 'Incorrect', wrong_vectors[i][0], sim[0][0]])
        # print('wrong similarity: {}'.format(np.array(result[k][1]).mean()))

        re = sorted(result, key=lambda x:x[3], reverse=True)[:10]
        print(re)

if __name__ == '__main__':
    calculate_distribution2()

