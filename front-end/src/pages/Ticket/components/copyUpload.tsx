import React, { useState } from 'react';

const FilePasteUpload: React.FC<{ handleUpload: (file: any) => void }> = (handleUpload) => {
  const [file, setFile] = useState<File | null>(null);
  const [imagePreview, setImagePreview] = useState<string | null>(null);

  const handlePaste = (event: React.ClipboardEvent) => {
    const items = event.clipboardData.items;
    for (const item of items) {
      if (item.kind === 'file') {
        const pastedFile = item.getAsFile();
        if (pastedFile) {
          setFile(pastedFile);

          // 如果是图片文件，生成预览图
          if (pastedFile.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = (e) => {
              setImagePreview(e.target?.result as string);
            };
            reader.readAsDataURL(pastedFile);
          }

          console.log('文件已粘贴:', pastedFile);
        }
      }
    }
  };

  const uploadFileInput = () => {
    if (file) {
      const formData = new FormData();
      formData.append('file', file);

      // 这里替换为你的上传API
      fetch('http://47.116.201.99:8001/test/upload_file', {
        method: 'POST',
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          console.log('data ', data);
          handleUpload.handleUpload(data);
        })
        .catch((error) => console.error('上传错误:', error));
    }
  };

  return (
    <div>
      <input type="text" onPaste={handlePaste} placeholder="在这里粘贴文件" />
      {imagePreview && (
        <div>
          <img src={imagePreview} alt="文件预览" width="200" />
        </div>
      )}
      {file && (
        <div>
          <button onClick={uploadFileInput}>上传文件</button>
        </div>
      )}
    </div>
  );
};

export default FilePasteUpload;
