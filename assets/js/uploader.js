const videoUploader = document.querySelector('#video-uploader');
const videoPlayer = document.querySelector('#video-player');
const uploadedVideo = document.querySelector('#uploaded-video');
const uploadButton = document.querySelector('#upload-button');
const videoDesc = document.querySelector('#video-desc');
const videoDetails = document.querySelector('#video-details');
const fileInfo = document.querySelector('#file-info');

uploadButton.addEventListener('click', () => {
  const videoFile = videoUploader.querySelector('#video-file').files[0];
  const videoDescText = videoDesc.value;

  if (videoFile) {
    const videoURL = URL.createObjectURL(videoFile);

    uploadedVideo.src = videoURL;
    videoDetails.textContent = `Video Description: ${videoDescText}`;

    videoPlayer.style.display = 'block';

    // Show the file name in fileInfo
    fileInfo.textContent = `File Name: ${videoFile.name}`;
  } else {
    // Handle the case when no file is selected
    Swal.fire({
      title: 'Error',
      text: 'Please select a video file.',
      icon: 'error',
      confirmButtonText: 'OK',
    });
  }
});

uploadedVideo.addEventListener('loadeddata', () => {
  uploadedVideo.play();

  // Reset values after uploading
  videoDesc.value = '';
  videoUploader.querySelector('#video-file').value = '';
  fileInfo.textContent = '';

  // Show upload success alert
  Swal.fire({
    title: 'Upload Successful!',
    text: 'Your video has been uploaded successfully!',
    icon: 'success',
    confirmButtonText: 'OK',
  });
});
